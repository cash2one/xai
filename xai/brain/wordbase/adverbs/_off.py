

#calss header
class _OFF():
	def __init__(self,): 
		self.name = "OFF"
		self.definitions = [u'away from a place or position, especially the present place, position, or time: ', u'used with actions in which something is removed or removes itself from another thing: ', u'(especially of machines, electrical devices, lights, etc.) not operating because of not being switched on: ', u'(of money) taken away from the original price: ', u'not at work; at home or on holiday: ', u'in such a way as to be separated: ', u'in such a way as to be completely absent, especially because of having been used or killed: ', u'in such a way as to get rid of something: ', u'used to form nouns referring to a situation in which two or more people or teams compete against each other to see who is the winner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
