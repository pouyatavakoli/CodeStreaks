from CodeStreaks.logger import configure_logger
import requests

logger = configure_logger(__name__)

def get_user_submissions(handle):
    """Fetch user submissions from Codeforces API with detailed logging."""
    try:
        # Start tracking progress
        #logger.info(f"Starting submissions fetch for {handle}")
        
        # API request
        url = f"https://codeforces.com/api/user.status?handle={handle}"
        response = requests.get(url)
        logger.debug(f"Response received - Status: {response.status_code}")
        
        # Check HTTP status
        response.raise_for_status()
        
        # Parse JSON data
        data = response.json()
        logger.debug(f"Raw API response: {data}")
        
        # Check API status
        if data['status'] != 'OK':
            error_msg = data.get('comment', 'Unknown API error')
            logger.error(f"API Error for {handle}: {error_msg}")
            raise Exception(f"API Error: {error_msg}")
        
        # Process successful response
        submissions = data['result']
        #logger.info(f"Successfully retrieved {len(submissions)} submissions for {handle}")
        return submissions

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error for {handle}: {str(e)}")
        raise
    except ValueError as e:
        logger.error(f"JSON parsing error for {handle}: {str(e)}")
        raise
    except KeyError as e:
        logger.error(f"Missing expected data key for {handle}: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error processing {handle}: {str(e)}", exc_info=True)
        raise