

#calss header
class _GOOD():
	def __init__(self,): 
		self.name = "GOOD"
		self.definitions = [u'very satisfactory, enjoyable, pleasant, or interesting: ', u'used in greetings: ', u'healthy or well: ', u'used as a general reply when someone greets you: ', u'of a high quality or level: ', u'used to express praise: ', u'successful, or able to do something well: ', u'to be of low quality or not useful: ', u'to begin an activity successfully: ', u'kind or helpful: ', u'used to make a polite request: ', u'to do something kind that helps someone else', u'morally right or based on religious principles: ', u'having a positive or useful effect, especially on the health: ', u'A good child or animal behaves well: ', u'able to be trusted: ', u'suitable, convenient, or satisfactory: ', u'used to emphasize the large number, amount, or level of something: ', u'much: ', u'more than: ', u'said when you are satisfied or pleased about something, or to show agreement with a decision: ', u'used to tell someone that you have everything that you need: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
