class ListNode:
    def __init__(self,value,next=None):
        self.value = value   # düğümün tuttuğu veri
        self.next = next     # bir SONRAKİ düğümün adresi (bağlantı)

def print_list(head):
    p = head                # listeyi gezmek için pointer
    while p is not None:    # None → listenin sonu demek
        print(p.value)      
        p = p.next          # bir sonraki düğüme geç

def append_element(head,value):
   node = ListNode(value)   # eklenecek yeni düğüm
   if head is None:         # liste boşsa direkt head o olur
       head = node
   else:
        p = head
        while p.next is not None:  # listenin sonuna kadar git
            p = p.next
        p.next = node       # son düğümün next'ine yeni düğümü bağla

# 3 düğüm oluşturduk
node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(2)

node1.next = node2   # 4 → 1
node2.next = node3   # 1 → 2

head = node1
print("before:")
print_list(head)

append_element(head,3)  # sona 3 ekle
print("after:")
print_list(head)
