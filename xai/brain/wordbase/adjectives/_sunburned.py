

#calss header
class _SUNBURNED():
	def __init__(self,): 
		self.name = "SUNBURNED"
		self.definitions = [u'Sunburned skin has become red and sore by being in the strong heat of the sun for too long, or is very suntanned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
