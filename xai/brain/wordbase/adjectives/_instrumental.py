

#calss header
class _INSTRUMENTAL():
	def __init__(self,): 
		self.name = "INSTRUMENTAL"
		self.definitions = [u'If someone or something is instrumental in a process, plan, or system, that person or thing is one of the most important influences in causing it to happen: ', u'involving only musical instruments, and no singing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
