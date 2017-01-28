

#calss header
class _UNDETERRED():
	def __init__(self,): 
		self.name = "UNDETERRED"
		self.definitions = [u'still continuing to do something or enthusiastic about doing it despite a bad situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
