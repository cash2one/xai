

#calss header
class _SCRIPTED():
	def __init__(self,): 
		self.name = "SCRIPTED"
		self.definitions = [u'A scripted speech or broadcast has been written before it is read or performed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
