

#calss header
class _LUKEWARM():
	def __init__(self,): 
		self.name = "LUKEWARM"
		self.definitions = [u'(especially of a liquid) only slightly warm: ', u'not enthusiastic or interested: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
