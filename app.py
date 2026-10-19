import os, sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from algorithms import bubble_sort, insertion_sort, merge_sort, linear_search, binary_search, PriorityQueue

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "student-demo-secret")
DB = os.path.join(os.path.dirname(__file__), "baggage.db")
STATUSES = ["Registered", "Queued", "Processing", "Sorted", "Dispatched"]
PRIORITIES = ["Normal", "Priority", "Urgent"]

def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with db() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS bags(
          id INTEGER PRIMARY KEY AUTOINCREMENT, passenger TEXT NOT NULL, flight TEXT NOT NULL,
          destination TEXT NOT NULL, weight REAL NOT NULL, priority TEXT NOT NULL,
          status TEXT NOT NULL, created_at TEXT NOT NULL)""")
        if con.execute("SELECT COUNT(*) FROM bags").fetchone()[0] == 0:
            demo = [
              ("Aarav Sharma","AI 602","Delhi",18.4,"Normal","Registered"),
              ("Meera Joshi","6E 214","Mumbai",12.2,"Urgent","Queued"),
              ("Kabir Khan","UK 811","Bengaluru",21.0,"Priority","Processing"),
              ("Ananya Patil","AI 431","Pune",15.7,"Normal","Sorted"),
              ("Rohan Das","6E 901","Hyderabad",19.3,"Priority","Queued")]
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            con.executemany("INSERT INTO bags(passenger,flight,destination,weight,priority,status,created_at) VALUES(?,?,?,?,?,?,?)",
                            [x+(now,) for x in demo])

def all_bags():
    with db() as con:
        return [dict(r) for r in con.execute("SELECT * FROM bags ORDER BY id").fetchall()]

@app.route("/")
def home():
    bags = all_bags()
    stats = {s: sum(b["status"] == s for b in bags) for s in STATUSES}
    return render_template("index.html", bags=bags[-5:][::-1], total=len(bags), stats=stats)

@app.route("/baggage", methods=["GET","POST"])
def baggage():
    if request.method == "POST":
        passenger=request.form.get("passenger","").strip()
        flight=request.form.get("flight","").strip().upper()
        dest=request.form.get("destination","").strip()
        priority=request.form.get("priority","Normal")
        try: weight=float(request.form.get("weight","0"))
        except ValueError: weight=0
        if not passenger or not flight or not dest or weight <= 0 or priority not in PRIORITIES:
            flash("Please enter valid baggage details. Weight must be above zero.","error")
        else:
            with db() as con:
                con.execute("INSERT INTO bags(passenger,flight,destination,weight,priority,status,created_at) VALUES(?,?,?,?,?,'Registered',?)",
                            (passenger,flight,dest,weight,priority,datetime.now().strftime("%Y-%m-%d %H:%M")))
            flash("Baggage successfully registered.","success")
        return redirect(url_for("baggage"))
    q=request.args.get("q","").strip()
    sort=request.args.get("sort","newest")
    bags=all_bags()
    if q: bags=linear_search(bags,q)
    if sort=="weight": bags=merge_sort(bags,"weight")
    elif sort=="passenger": bags=insertion_sort(bags,"passenger")
    elif sort=="priority":
        rank={"Urgent":0,"Priority":1,"Normal":2}
        bags=bubble_sort(bags,lambda b:rank[b["priority"]])
    elif sort=="newest": bags.reverse()
    return render_template("baggage.html",bags=bags,q=q,sort=sort,statuses=STATUSES,priorities=PRIORITIES)

@app.post("/status/<int:bag_id>")
def status(bag_id):
    value=request.form.get("status")
    if value in STATUSES:
        with db() as con: con.execute("UPDATE bags SET status=? WHERE id=?",(value,bag_id))
        flash("Baggage status updated.","success")
    return redirect(url_for("baggage"))

@app.post("/delete/<int:bag_id>")
def delete(bag_id):
    with db() as con: con.execute("DELETE FROM bags WHERE id=?",(bag_id,))
    flash("Baggage record deleted.","success")
    return redirect(url_for("baggage"))

@app.route("/sorting")
def sorting():
    method=request.args.get("method","merge")
    bags=all_bags()
    if method=="bubble":
        result=bubble_sort(bags,lambda b:b["id"]); title="Bubble Sort"; complexity="O(n²)"
        explanation="Compares adjacent records and swaps them when they are out of order."
    elif method=="insertion":
        result=insertion_sort(bags,"weight"); title="Insertion Sort by weight"; complexity="O(n²)"
        explanation="Inserts each baggage record into its correct place in the sorted section."
    else:
        result=merge_sort(bags,"weight"); title="Merge Sort by weight"; complexity="O(n log n)"
        explanation="Splits records into smaller lists, sorts each half and merges them."
    return render_template("sorting.html",bags=result,method=method,title=title,complexity=complexity,explanation=explanation)

@app.route("/tracking", methods=["GET","POST"])
def tracking():
    result=None; q=""; method="binary"
    if request.method=="POST":
        q=request.form.get("q","").strip(); method=request.form.get("method","binary")
        bags=all_bags()
        if method=="binary":
            try: result=binary_search(bags,int(q.replace("AS-","").replace("as-","")))
            except ValueError: result=None
        else:
            found=linear_search(bags,q)
            result=found[0] if found else None
        if result is None: flash("No matching baggage found.","error")
    return render_template("tracking.html",result=result,q=q,method=method)

@app.route("/queue",methods=["GET","POST"])
def queue():
    if request.method=="POST":
        action=request.form.get("action")
        with db() as con:
            if action=="enqueue":
                con.execute("UPDATE bags SET status='Queued' WHERE id=? AND status='Registered'",(request.form.get("id"),))
                flash("Registered bag added to queue, if eligible.","success")
            elif action=="process":
                rows=[dict(r) for r in con.execute("SELECT * FROM bags WHERE status='Queued'").fetchall()]
                pq=PriorityQueue()
                for row in rows: pq.enqueue(row)
                next_bag=pq.dequeue()
                if next_bag:
                    con.execute("UPDATE bags SET status='Processing' WHERE id=?",(next_bag["id"],))
                    flash("Priority queue selected baggage AS-%04d." % next_bag["id"],"success")
                else: flash("Queue is empty.","error")
        return redirect(url_for("queue"))
    bags=all_bags()
    registered=[b for b in bags if b["status"]=="Registered"]
    queued=PriorityQueue()
    for b in bags:
        if b["status"]=="Queued": queued.enqueue(b)
    return render_template("queue.html",registered=registered,queued=queued.items)

@app.route("/about")
def about(): return render_template("about.html")

if __name__=="__main__":
    init_db()
    app.run(debug=True,port=5000)
