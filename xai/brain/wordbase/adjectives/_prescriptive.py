

#calss header
class _PRESCRIPTIVE():
	def __init__(self,): 
		self.name = "PRESCRIPTIVE"
		self.definitions = [u'saying exactly what must happen, especially by giving an instruction or making a rule: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
