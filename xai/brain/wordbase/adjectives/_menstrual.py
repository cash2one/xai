

#calss header
class _MENSTRUAL():
	def __init__(self,): 
		self.name = "MENSTRUAL"
		self.definitions = [u'connected with the time when a woman menstruates: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
