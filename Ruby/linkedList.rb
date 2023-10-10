class LinkedList
    attr_accessor :head

    def initialize
        self.head = nil
    end

    def add(value)
        if (self.head.nil?)
            self.head = Node.new(value,nil)
        else
            lastNode = self.head
            while(!lastNode.nextNode.nil?)
                lastNode = lastNode.nextNode
            end
            lastNode.nextNode = Node.new(value,nil)
        end
    end

    def find(value)
        node = self.head
        while(!node.nextNode.nil?)
            if node.val == value
                return true
            end
            node = node.nextNode
        end
        false
    end


    private
    class Node
        attr_accessor :val , :nextNode
        def initialize(val,nextNode)
           self.val = val 
           self.nextNode = nextNode   
        end
    end
end

ll = LinkedList.new
ll.add(10)
ll.add(20)
ll.add(30)
puts ll.head.val
puts ll.head.nextNode.val
puts ll.find(10)
puts ll.find(90)
