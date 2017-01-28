

#calss header
class _COLD():
	def __init__(self,): 
		self.name = "COLD"
		self.definitions = [u'at a low temperature, especially when compared to the temperature of the human body, and not hot, or warm: ', u'not showing kindness, love, or emotion and not friendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
