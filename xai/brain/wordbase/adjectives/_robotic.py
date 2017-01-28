

#calss header
class _ROBOTIC():
	def __init__(self,): 
		self.name = "ROBOTIC"
		self.definitions = [u'relating to or like a robot', u'Robotic dancing is dancing in which you make short sudden movements with your arms and legs like the actions of a robot.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
