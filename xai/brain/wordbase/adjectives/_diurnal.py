

#calss header
class _DIURNAL():
	def __init__(self,): 
		self.name = "DIURNAL"
		self.definitions = [u'happening over a period of a day, or being active or happening during the day rather than at night']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
