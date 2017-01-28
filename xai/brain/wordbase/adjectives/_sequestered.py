

#calss header
class _SEQUESTERED():
	def __init__(self,): 
		self.name = "SEQUESTERED"
		self.definitions = [u'A sequestered place is peaceful because it is far away from people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
