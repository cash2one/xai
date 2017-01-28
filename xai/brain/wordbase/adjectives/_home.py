

#calss header
class _HOME():
	def __init__(self,): 
		self.name = "HOME"
		self.definitions = [u'relating to the house, flat, etc. where someone lives: ', u'done at home, or intended to be used at home: ', u'relating to your family or your life at home: ', u'connected with or done in your own country: ', u'relating to the place where a team is based and plays a lot of its games: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
