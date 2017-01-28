

#calss header
class _ERECT():
	def __init__(self,): 
		self.name = "ERECT"
		self.definitions = [u'standing with your back and neck very straight: ', u'When a part of the body, especially soft tissue, is erect, it is harder and bigger than usual, often pointing out or up: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
