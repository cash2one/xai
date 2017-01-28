

#calss header
class _DOMESTICATED():
	def __init__(self,): 
		self.name = "DOMESTICATED"
		self.definitions = [u'(of animals or plants) brought under human control in order to provide food, power, or company: ', u'able or willing to do cleaning, cooking, and other jobs in the home, and to take care of children: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
