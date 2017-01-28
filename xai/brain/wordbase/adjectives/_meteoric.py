

#calss header
class _METEORIC():
	def __init__(self,): 
		self.name = "METEORIC"
		self.definitions = [u'relating to or caused by a meteor: ', u'used to describe something that develops very fast and attracts a lot of attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
