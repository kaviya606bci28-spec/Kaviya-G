from collections import namedtuple, defaultdict, Counter, deque, OrderedDict

# Setup
Book = namedtuple('Book', ['id', 'title', 'author', 'genre', 'copies'])
lib, genres, b_count, g_count, wait = OrderedDict(), defaultdict(list), Counter(), Counter(), defaultdict(deque)

def add_book(id, t, a, g, c):
    lib[id] = Book(id, t, a, g, c)
    genres[g].append(t)

def borrow_book(user, id):
    b = lib[id]
    if b.copies > 0:
        lib[id] = b._replace(copies=b.copies - 1)
        b_count[id] += 1; g_count[b.genre] += 1
        print(f"{user} borrowed {b.title}")
    else:
        wait[id].append(user)
        print(f"{user} added to waiting list for {b.title}")

def return_book(id):
    if wait[id]:
        user = wait[id].popleft()
        b_count[id] += 1
        print(f"Book given to waiting user: {user}")
    else:
        lib[id] = lib[id]._replace(copies=lib[id].copies + 1)
        print("Book returned to shelf")


