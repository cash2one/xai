

#calss header
class _ULTRASONIC():
	def __init__(self,): 
		self.name = "ULTRASONIC"
		self.definitions = [u'Ultrasonic sound is too high for people to hear.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
