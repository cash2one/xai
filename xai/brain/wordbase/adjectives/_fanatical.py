

#calss header
class _FANATICAL():
	def __init__(self,): 
		self.name = "FANATICAL"
		self.definitions = [u'extremely interested in something, to a degree that someone people find unreasonable: ', u'holding extreme beliefs that may lead to unreasonable or violent behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
