

#calss header
class _UNPERTURBED():
	def __init__(self,): 
		self.name = "UNPERTURBED"
		self.definitions = [u'not worried about something, especially when this is slightly surprising: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
