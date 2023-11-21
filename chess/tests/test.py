class Aplication:
    def __init__(self,actions) -> None:
        #parser=Parser()
        #self.arguments  = parser.parse_args()
        self.actions=actions
    def main(self):
        match self.arguments.action:
            case 'add_expense':
                self.add_expense(self.arguments.name,self.arguments.category,self.arguments.date,self.arguments.value)
            case 'add_income':
                self.add_income(self.arguments.name,self.arguments.category,self.arguments.date,self.arguments.value)
            case 'delete':
                self.delete(self.arguments.id)
            case 'list':
                self.list()     
            case 'stats':
                self.stats()
    def add_expense(self,name,category,date,value):
        self.actions.add_item(name, category, date, -(int(value)))
    def add_income(self,name,category,date,value):
        self.actions.add_item(name, category, date, value)
    def delete(self,id):
        self.actions.delete_item(id)
    def list(self):
        for n in self.actions.list_items():
            print(n)
    def stats(self):
        print(self.actions.stats()[0])