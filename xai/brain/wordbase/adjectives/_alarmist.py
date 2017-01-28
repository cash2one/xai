

#calss header
class _ALARMIST():
	def __init__(self,): 
		self.name = "ALARMIST"
		self.definitions = [u'intentionally showing only the bad and dangerous things in a situation, and so worrying people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
