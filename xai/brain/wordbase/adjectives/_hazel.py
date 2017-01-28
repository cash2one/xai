

#calss header
class _HAZEL():
	def __init__(self,): 
		self.name = "HAZEL"
		self.definitions = [u'(especially of eyes) greenish-brown or yellowish-brown in colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
