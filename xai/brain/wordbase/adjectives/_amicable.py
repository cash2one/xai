

#calss header
class _AMICABLE():
	def __init__(self,): 
		self.name = "AMICABLE"
		self.definitions = [u'relating to behaviour between people that is pleasant and friendly, often despite a difficult situation: ', u'relating to an agreement or decision that is achieved without people arguing or being unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
