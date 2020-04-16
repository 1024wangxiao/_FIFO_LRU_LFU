from 缓存置换算法.DoubleLinkList import DoubleLinkedList,Node

class LFUNode(Node):
    def __init__(self,key,value):
        self.freq=0
        super(LFUNode,self).__init__(key,value)

class LFUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.map={}
        self.size=0
        #key是频率，value是频率所对应的双向链表
        self.freq_map={}
        #更新结点频率的操作
    def __update_freq(self,node):
        freq=node.freq
        #删除
        ndoe = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size==0:
            del self.freq_map[freq]
        #更新
        freq+=1
        node.freq=freq
        if freq not in self.freq_map:
            self.freq_map[freq]=DoubleLinkedList()
        self.freq_map[freq].append(node)
    def get(self,key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__update_freq(node)
        return node.value
    def put(self,key,value):
        if self.capacity==0:
            return
        #缓存命中
        if key in self.map:
            node = self.map.get(key)
            node.value=value
            self.__update_freq(node)
        #缓存没有命中
        else:
            if self.capacity==self.size:
                min_freq=min(self.freq_map)
                node = self.freq_map[min_freq].pop()
                del self.map[node.key]
                self.size-=1
            node = LFUNode(key,value)
            node.freq = 1
            self.map[key]=node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            node = self.freq_map[node.freq].append(node)
            self.size+=1
    def print(self):
        print("*****************")
        for k ,v in self.freq_map.items():
            print("Freq= %d "%k)
            self.freq_map[k].print()
        print("*****************")
        print()

if __name__=="__main__":
    cache = LFUCache(2)
    cache.put(1,1)
    cache.print()
    cache.put(2,2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3,3)
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.put(4,4)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()




