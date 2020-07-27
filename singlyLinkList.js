class ListNode{
    constructor(data){
        this.data = data
        this.next = null
}
class LinkList{
    constructor(){
        this.head = null
        this._length = 0
    }
    addNode(data){
        var newNode = new ListNode(data)
        var currentNode 
        // if list is empty
        if(this.head = null){
            this.head = newNode
            this._length++
            return newNode
        }
        else{
            currentNode = this.head
            while(currentNode.next){
                currentNode = currentNode.next;
            }
            currentNode.next = newNode;
            this._length;
            return newNode
        }
    }
    insertNodeAt(data, index){
        if(index > 0 && index > this._length){
            return false
            
        }
    }
}

