

#calss header
class _SANITARY():
	def __init__(self,): 
		self.name = "SANITARY"
		self.definitions = [u'clean and not dangerous for your health, or protecting health by removing dirt and waste, especially human waste: ', u'used to refer to the things used by women during their period (= blood flow each month): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
