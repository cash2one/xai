

#calss header
class _CLEANSING():
	def __init__(self,): 
		self.name = "CLEANSING"
		self.definitions = [u'used to describe something that cleans or is used for cleaning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
