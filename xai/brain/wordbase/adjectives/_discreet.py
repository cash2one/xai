

#calss header
class _DISCREET():
	def __init__(self,): 
		self.name = "DISCREET"
		self.definitions = [u'careful not to cause embarrassment or attract too much attention, especially by keeping something secret: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
