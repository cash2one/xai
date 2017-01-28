

#calss header
class _INTESTATE():
	def __init__(self,): 
		self.name = "INTESTATE"
		self.definitions = [u'If someone dies intestate, they have died without leaving instructions about who should receive their property: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
