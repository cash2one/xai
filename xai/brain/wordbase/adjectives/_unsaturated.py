

#calss header
class _UNSATURATED():
	def __init__(self,): 
		self.name = "UNSATURATED"
		self.definitions = [u'Unsaturated fat or oil is either monounsaturated or polyunsaturated, found in plants, vegetable oil, and fish, and thought to be better for your health than saturated fat.', u'containing less of a substance than can be absorbed, and therefore not in a state of balance', u'used to describe a hydrocarbon in which the carbon atoms do not join as many hydrogen atoms as possible']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
