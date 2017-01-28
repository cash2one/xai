

#calss header
class _ASLEEP():
	def __init__(self,): 
		self.name = "ASLEEP"
		self.definitions = [u'sleeping or not awake: ', u'If your arm or leg is asleep, it cannot feel anything because it has been in the same position for so long.', u'to start to sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
