

#calss header
class _VENAL():
	def __init__(self,): 
		self.name = "VENAL"
		self.definitions = [u'A venal person is willing to behave in a way that is not honest or moral in exchange for money: ', u'A venal activity is done in order to get money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
