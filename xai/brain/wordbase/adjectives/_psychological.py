

#calss header
class _PSYCHOLOGICAL():
	def __init__(self,): 
		self.name = "PSYCHOLOGICAL"
		self.definitions = [u'relating to the human mind and feelings: ', u'(of an illness or other physical problem) caused by worry or sadness: ', u"A psychological film or book is one in which there is a lot of attention given to the way people influence each other's behaviour: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
