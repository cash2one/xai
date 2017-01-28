

#calss header
class _FURTHER():
	def __init__(self,): 
		self.name = "FURTHER"
		self.definitions = [u'comparative of  far : to a greater distance or degree, or at a more advanced level: ', u'If you go or take something further, you take it to a more advanced stage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
