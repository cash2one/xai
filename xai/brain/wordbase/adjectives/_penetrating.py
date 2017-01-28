

#calss header
class _PENETRATING():
	def __init__(self,): 
		self.name = "PENETRATING"
		self.definitions = [u'very loud: ', u'used to describe a way of looking at someone in which you seem to know what they are thinking', u'a mind that understands things quickly and well']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
