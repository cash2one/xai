

#calss header
class _RA():
	def __init__(self,): 
		self.name = "RA"
		self.definitions = [u'abbreviation for radial artery: the artery (= large blood vessel) that goes from below the elbow to the palm of the hand']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
