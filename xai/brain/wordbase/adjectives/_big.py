

#calss header
class _BIG():
	def __init__(self,): 
		self.name = "BIG"
		self.definitions = [u'large in size or amount: ', u'older or more like an adult: ', u'used to add emphasis: ', u'important, because of being powerful, or having a lot of influence or a serious effect: ', u'to be important or famous in a particular place or type of work: ', u'If a product or activity is big, it is extremely popular: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
