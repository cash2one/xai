

#calss header
class _EVEN():
	def __init__(self,): 
		self.name = "EVEN"
		self.definitions = [u'used to show that something is surprising, unusual, unexpected, or extreme: ', u'at the same time as: ', u'used to say that if something is the case or not, the result is the same: ', u'despite something: ', u'despite what has just been said: ', u'although: ', u'used to emphasize a comparison: ', u'used when you want to be more exact or detailed about something you have just said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
