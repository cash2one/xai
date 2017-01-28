

#calss header
class _ABLE():
	def __init__(self,): 
		self.name = "ABLE"
		self.definitions = [u'to have the necessary physical strength, mental power, skill, time, money, or opportunity to do something: ', u'to find it easier to do something: ', u'intelligent or good at what you do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
