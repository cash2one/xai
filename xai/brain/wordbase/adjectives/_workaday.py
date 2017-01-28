

#calss header
class _WORKADAY():
	def __init__(self,): 
		self.name = "WORKADAY"
		self.definitions = [u'ordinary; not unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
