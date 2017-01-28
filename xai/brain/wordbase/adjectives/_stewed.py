

#calss header
class _STEWED():
	def __init__(self,): 
		self.name = "STEWED"
		self.definitions = [u'cooked slowly in a small amount of liquid: ', u'Stewed tea has been kept too long before it is poured, and is therefore strong and bitter.', u'drunk']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
