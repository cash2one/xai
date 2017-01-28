

#calss header
class _FALLEN():
	def __init__(self,): 
		self.name = "FALLEN"
		self.definitions = [u'lying on the ground, after falling down: ', u'having dropped down: ', u'used to refer to someone who has been defeated or has lost a position of power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
