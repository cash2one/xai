

#calss header
class _HOSTILE():
	def __init__(self,): 
		self.name = "HOSTILE"
		self.definitions = [u'unfriendly and not liking something: ', u'not agreeing with something: ', u'difficult or not suitable for living or growing: ', u'connected with the enemy in a war: ', u'relating to situations in which one company wants to buy another company whose owners do not want to sell it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
