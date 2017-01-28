

#calss header
class _MENIAL():
	def __init__(self,): 
		self.name = "MENIAL"
		self.definitions = [u'Menial work is boring, makes you feel tired, and is given a low social value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
