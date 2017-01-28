

#calss header
class _COMMUNAL():
	def __init__(self,): 
		self.name = "COMMUNAL"
		self.definitions = [u'belonging to or used by a group of people rather than one single person: ', u'A communal society is one in which everyone lives and works together and property and possessions are shared rather than being owned by a particular person.', u'involving different social or religious groups within a community: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
