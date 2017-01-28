

#calss header
class _HEARTWARMING():
	def __init__(self,): 
		self.name = "HEARTWARMING"
		self.definitions = [u'(especially of an event, action, or story) seeming to be something positive and good and therefore causing feelings of pleasure and happiness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
