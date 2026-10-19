"""Sorting, searching and priority-queue implementations for the DSA project."""

def value(record, key):
    return key(record) if callable(key) else record[key]

def bubble_sort(records, key):
    a=list(records)
    for end in range(len(a)-1,0,-1):
        changed=False
        for i in range(end):
            if value(a[i],key)>value(a[i+1],key):
                a[i],a[i+1]=a[i+1],a[i]; changed=True
        if not changed: break
    return a

def insertion_sort(records,key):
    a=list(records)
    for i in range(1,len(a)):
        current=a[i]; j=i-1
        while j>=0 and value(a[j],key)>value(current,key):
            a[j+1]=a[j]; j-=1
        a[j+1]=current
    return a

def merge_sort(records,key):
    a=list(records)
    if len(a)<=1: return a
    mid=len(a)//2; left=merge_sort(a[:mid],key); right=merge_sort(a[mid:],key)
    result=[]; i=j=0
    while i<len(left) and j<len(right):
        if value(left[i],key)<=value(right[j],key): result.append(left[i]); i+=1
        else: result.append(right[j]); j+=1
    return result+left[i:]+right[j:]

def linear_search(records,term):
    term=str(term).lower()
    fields=("id","passenger","flight","destination","status","priority")
    return [r for r in records if any(term in str(r.get(k,"")).lower() for k in fields)]

def binary_search(records, target_id):
    # The database returns records in ascending ID order.
    low,high=0,len(records)-1
    while low<=high:
        mid=(low+high)//2; found=int(records[mid]["id"])
        if found==target_id: return records[mid]
        if found<target_id: low=mid+1
        else: high=mid-1
    return None

class PriorityQueue:
    """Educational priority queue: Urgent, then Priority, then Normal; FIFO within a tier."""
    rank={"Urgent":0,"Priority":1,"Normal":2}
    def __init__(self): self.items=[]
    def enqueue(self,item):
        self.items.append(item)
        self.items.sort(key=lambda x:(self.rank.get(x.get("priority","Normal"),2),x.get("id",0)))
    def dequeue(self): return self.items.pop(0) if self.items else None
    def peek(self): return self.items[0] if self.items else None
    def is_empty(self): return not self.items
