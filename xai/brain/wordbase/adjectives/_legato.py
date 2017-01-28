

#calss header
class _LEGATO():
	def __init__(self,): 
		self.name = "LEGATO"
		self.definitions = [u'used to describe music that is played in a smooth, continuous way, or this way of playing music: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
