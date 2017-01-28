

#calss header
class _SATANIC():
	def __init__(self,): 
		self.name = "SATANIC"
		self.definitions = [u'connected with worshipping Satan: ', u'very evil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
